#!/bin/bash
# Populate prerequisites for knowledge graph
# Rule: each file in chN gets all titles from ch(N-1) as prerequisites
set -e

DOCS="E:/programcc408/cc408/content/docs"
declare -a FILES=()
declare -A SUBJ_CH_TITLES=()

echo "Scanning..."
while IFS= read -r -d '' FILE; do
    [[ "$(basename "$FILE")" == "_index.md" ]] && continue
    REL="${FILE#$DOCS/}"
    SUBJ="${REL%%/*}"
    CH_DIR="${REL#*/}"; CH_DIR="${CH_DIR%%/*}"
    [[ "$CH_DIR" != ch* ]] && continue

    # Extract chapter number: ch00-overview → 0, ch01-data → 1
    CH_STR="${CH_DIR#ch}"; CH_STR="${CH_STR%%-*}"
    CH_NUM=$((10#$CH_STR))

    TITLE=$(grep -m1 '^title:' "$FILE" | sed 's/^title: *"//; s/"$//' | xargs)
    [[ -z "$TITLE" ]] && TITLE="$(basename "$FILE" .md)"

    KEY="${SUBJ}/${CH_NUM}"
    if [[ -z "${SUBJ_CH_TITLES[$KEY]}" ]]; then
        SUBJ_CH_TITLES[$KEY]="$TITLE"
    else
        SUBJ_CH_TITLES[$KEY]="${SUBJ_CH_TITLES[$KEY]}|$TITLE"
    fi
    FILES+=("$FILE|$SUBJ|$CH_NUM")
done < <(find "$DOCS" -name '*.md' -not -name '_index.md' -print0 2>/dev/null)

echo "Found ${#FILES[@]} files"
echo ""

# Phase 2: apply prerequisites
MODIFIED=0
for ENTRY in "${FILES[@]}"; do
    FILE="${ENTRY%%|*}"; REST="${ENTRY#*|}"
    SUBJ="${REST%%|*}";  CH_NUM="${REST##*|}"
    [[ "$CH_NUM" == "0" ]] && continue

    PREV=$((CH_NUM - 1))
    PREV_ALL="${SUBJ_CH_TITLES[${SUBJ}/${PREV}]}"
    [[ -z "$PREV_ALL" ]] && continue

    # Build: prerequisites: ["Title1", "Title2"]
    REPLACE='prerequisites: ["'
    IFS='|' read -ra TITLES <<< "$PREV_ALL"
    REPLACE+="${TITLES[0]}"
    for ((t=1; t<${#TITLES[@]}; t++)); do
        REPLACE+='", "'
        REPLACE+="${TITLES[$t]}"
    done
    REPLACE+='"]'

    sed -i "s|^prerequisites: \[\]|$REPLACE|" "$FILE"
    echo "  $(basename "$FILE") ← $(echo "$PREV_ALL" | tr '|' ', ')"
    MODIFIED=$((MODIFIED + 1))
done

echo ""
echo "Done! Modified $MODIFIED files."
