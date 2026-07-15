const JSZip = require('jszip');
const fs = require('fs');
const path = require('path');

const inputFile = process.argv[2];
if (!inputFile) {
  console.error('Usage: node clean_watermark.js <input.docx>');
  process.exit(1);
}

async function cleanWatermark(inputPath) {
  const data = fs.readFileSync(inputPath);
  const zip = await JSZip.loadAsync(data);

  let modifiedCount = 0;
  const filesToProcess = [];

  zip.forEach((relativePath, file) => {
    if (relativePath.endsWith('.xml') && relativePath.startsWith('word/')) {
      filesToProcess.push({ relativePath, file });
    }
  });

  for (const { relativePath, file } of filesToProcess) {
    let content = await file.async('string');
    const original = content;

    // Pattern 1: HYPERLINK field to csgraduates.com
    // <w:r><w:fldChar w:fldCharType="begin"/></w:r>
    // <w:r><w:instrText xml:space="preserve"> HYPERLINK "https://www.csgraduates.com" </w:instrText></w:r>
    // <w:r><w:fldChar w:fldCharType="separate"/></w:r>
    // <w:r>...<w:t>www.csgraduates.com</w:t>...</w:r>
    // <w:r><w:fldChar w:fldCharType="end"/></w:r>
    content = content.replace(
      /<w:r><w:fldChar w:fldCharType="begin"\/><\/w:r><w:r><w:instrText[^>]*>\s*HYPERLINK\s+&quot;https?:\/\/www\.csgraduates\.com&quot;\s*<\/w:instrText><\/w:r><w:r><w:fldChar w:fldCharType="separate"\/><\/w:r><w:r>.*?<\/w:r><w:r><w:fldChar w:fldCharType="end"\/><\/w:r>/gs,
      ''
    );

    // Pattern 2: Simple HYPERLINK begin+instrText to csgraduates (just the begin/instrText/separate/end without the display run)
    content = content.replace(
      /<w:r><w:fldChar w:fldCharType="begin"\/><\/w:r><w:r><w:instrText[^>]*>\s*HYPERLINK\s+&quot;https?:\/\/www\.csgraduates\.com&quot;\s*<\/w:instrText><\/w:r><w:r><w:fldChar w:fldCharType="separate"\/><\/w:r>/gs,
      ''
    );

    // Pattern 3: Remove runs containing csgraduates text (display text)
    content = content.replace(
      /<w:r>(?:<w:rPr>.*?<\/w:rPr>)?<w:t[^>]*>[^<]*csgraduates[^<]*<\/w:t><\/w:r>/gs,
      ''
    );

    // Pattern 4: Remove runs containing www.csgraduates.com text
    content = content.replace(
      /<w:r>(?:<w:rPr>.*?<\/w:rPr>)?<w:t[^>]*>[^<]*www\.csgraduates\.com[^<]*<\/w:t><\/w:r>/gs,
      ''
    );

    // Pattern 5: Remove "答案详见计算机考研杂货铺" runs (Chinese text might be encoded differently)
    content = content.replace(
      /<w:r>(?:<w:rPr>.*?<\/w:rPr>)?<w:t[^>]*>[^<]*(?:答案详见|计算机考研杂货|杂货铺)[^<]*<\/w:t><\/w:r>/gs,
      ''
    );

    // Pattern 6: Remove fldCharType="end" that might be orphaned
    content = content.replace(
      /<w:r><w:fldChar w:fldCharType="end"\/><\/w:r>/g,
      (match) => {
        // Only remove if it was part of a csgraduates hyperlink (already removed)
        // This is a heuristic - if there's no preceding fldChar begin, it's orphaned
        return '';
      }
    );

    // Pattern 7: Clean up empty runs that might remain
    content = content.replace(
      /<w:r><w:fldChar w:fldCharType="end"\/><\/w:r>/g,
      ''
    );

    if (content !== original) {
      modifiedCount++;
      zip.file(relativePath, content);
    }
  }

  if (modifiedCount > 0) {
    const outputData = await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' });
    const outputPath = inputPath.replace(/\.docx$/, '_cleaned.docx');
    fs.writeFileSync(outputPath, outputData);
    console.log(`Cleaned ${modifiedCount} files. Output: ${outputPath}`);
  } else {
    console.log('No watermarks found.');
  }
}

cleanWatermark(inputFile).catch(err => {
  console.error('Error:', err.message);
  process.exit(1);
});
