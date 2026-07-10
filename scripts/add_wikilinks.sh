#!/bin/bash
# Add Obsidian wiki-links to docs content based on prerequisites
set -e

DOCS="E:/programcc408/cc408/content/docs"
declare -A TITLE_TO_FILE  # title -> filename (no .md)
declare -A FILE_PREREQS   # filepath -> prereq list (separated by ||)
declare -a ALL_FILES=()

# Phase 1: build title→filename map and collect file data
while IFS= read -r -d '' FILE; do
    [[ "$(basename "$FILE")" == "_index.md" ]] && continue
    FNAME="$(basename "$FILE" .md)"

    TITLE=$(grep -m1 '^title:' "$FILE" | sed 's/^title: *"//; s/"$//' | xargs)
    [[ -z "$TITLE" ]] && TITLE="$FNAME"

    TITLE_TO_FILE["$TITLE"]="$FNAME"

    # Extract prerequisites (JSON array format: ["T1", "T2"])
    PREREQ_LINE=$(grep -m1 '^prerequisites:' "$FILE" | sed 's/^prerequisites: \[//; s/\]$//' | xargs)
    if [[ -n "$PREREQ_LINE" && "$PREREQ_LINE" != "\[\]" ]]; then
        # Parse: "Title1", "Title2" → split by ", "
        FILE_PREREQS["$FILE"]="$PREREQ_LINE"
    fi
    ALL_FILES+=("$FILE")
done < <(find "$DOCS" -name '*.md' -not -name '_index.md' -print0 2>/dev/null)

echo "Title→File mapping: ${#TITLE_TO_FILE[@]} entries"
echo ""

# Phase 2: add wiki-links footer
MODIFIED=0
for FILE in "${ALL_FILES[@]}"; do
    PREREQS="${FILE_PREREQS[$FILE]}"
    [[ -z "$PREREQS" ]] && continue

    # Check if "相关笔记" section already exists
    if grep -q '^## 相关笔记' "$FILE" 2>/dev/null; then
        continue
    fi

    # Parse comma-separated quoted titles
    WIKI_LINKS=""
    while IFS=',' read -ra ITEMS; do
        for ITEM in "${ITEMS[@]}"; do
            # Clean up: remove quotes and spaces
            TITLE=$(echo "$ITEM" | sed 's/^ *"//; s/" *$//' | xargs)
            [[ -z "$TITLE" ]] && continue
            FNAME="${TITLE_TO_FILE[$TITLE]}"
            if [[ -n "$FNAME" ]]; then
                WIKI_LINKS="${WIKI_LINKS}- [[${FNAME}|${TITLE}]]\n"
            fi
        done
    done <<< "$PREREQS"

    # Remove trailing \n
    WIKI_LINKS="${WIKI_LINKS%\\n}"

    if [[ -n "$WIKI_LINKS" ]]; then
        echo -e "\n\n## 相关笔记\n\n${WIKI_LINKS}" >> "$FILE"
        echo "  $(basename "$FILE"): added wiki-links"
        MODIFIED=$((MODIFIED + 1))
    fi
done

echo ""
echo "Done! Modified $MODIFIED files."
