#!/bin/bash
# Add aliases to each doc's frontmatter so Obsidian shows Chinese names
set -e

DOCS="E:/programcc408/cc408/content/docs"
MODIFIED=0

while IFS= read -r -d '' FILE; do
    [[ "$(basename "$FILE")" == "_index.md" ]] && continue

    # Extract title
    TITLE=$(grep -m1 '^title:' "$FILE" | sed 's/^title: *"//; s/"$//' | xargs)
    [[ -z "$TITLE" ]] && continue

    # Check if aliases already exists
    if grep -q '^aliases:' "$FILE"; then
        continue
    fi

    # Insert aliases line after the title line
    # Format: title: "X" → title: "X"\naliases: ["X"]
    sed -i "/^title:/a\aliases: [\"$TITLE\"]" "$FILE"

    echo "  $(basename "$FILE") → aliases: [$TITLE]"
    MODIFIED=$((MODIFIED + 1))
done < <(find "$DOCS" -name '*.md' -not -name '_index.md' -print0 2>/dev/null)

echo ""
echo "Done! Modified $MODIFIED files."
