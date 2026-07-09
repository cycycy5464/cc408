BEGIN {
  subject = ""
  qnum = ""
  qcontent = ""
  subjects_seen["数据结构"] = 0
  subjects_seen["组成原理"] = 0
  subjects_seen["操作系统"] = 0
  subjects_seen["计算机网络"] = 0
  line_count = 0
}

# Skip frontmatter (between --- markers)
/^---$/ && line_count < 15 { frontmatter_active = !frontmatter_active; next }
frontmatter_active { next }

# Track subject headers
/^#### / {
  sub("^#### ", "")
  sub(" *$", "")
  new_subject = $0
  subjects_seen[new_subject]++
  # If we've seen this subject before, we're in the 大题 section
  if (subjects_seen[new_subject] > 1) {
    subject = new_subject "(大题)"
  } else {
    subject = new_subject
  }
  next  # Don't include subject header in question content
}

# Question number encountered
/^##### [0-9]+/ {
  # Output previous question if exists
  if (qnum != "") {
    write_question()
  }
  # Start new question
  split($0, parts, " ")
  qnum = parts[2]
  qcontent = ""
  next
}

# Accumulate content for current question
{
  if (qnum != "") {
    qcontent = qcontent $0 "\n"
  }
}

END {
  if (qnum != "") write_question()
}

function write_question() {
  # Determine question type
  qtype = "choice"
  if (int(qnum) >= 41) qtype = "comprehensive"

  # Extract actual subject (remove "(大题)" suffix)
  actual_subject = subject
  gsub(" \\(大题\\)", "", actual_subject)

  # Skip if no subject
  if (actual_subject == "") {
    qnum = ""
    qcontent = ""
    return
  }

  # Build filename
  subj_abbr = ""
  if (actual_subject == "数据结构") subj_abbr = "ds"
  else if (actual_subject == "计算机组成原理") subj_abbr = "co"
  else if (actual_subject == "操作系统") subj_abbr = "os"
  else if (actual_subject == "计算机网络") subj_abbr = "cn"

  num_padded = sprintf("%03d", int(qnum))
  filename = sprintf("%s/question/2009-%s-%s.md", SRC_DIR, subj_abbr, num_padded)

  # Determine difficulty (default 3 for 2009)
  difficulty = 3
  if (qtype == "comprehensive") difficulty = 4

  # Generate knowledge_points placeholder from subject
  kp = ""
  if (actual_subject == "数据结构") kp = "数据结构"
  else if (actual_subject == "计算机组成原理") kp = "计算机组成原理"
  else if (actual_subject == "操作系统") kp = "操作系统"
  else if (actual_subject == "计算机网络") kp = "计算机网络"

  # Build frontmatter
  print "---" > filename
  print sprintf("title: \"2009 %s 第%d题\"", actual_subject, int(qnum)) > filename
  print "date: 2026-07-03" > filename
  print "type: question" > filename
  print "years:" > filename
  print "  - \"2009\"" > filename
  print "subjects:" > filename
  print sprintf("  - \"%s\"", actual_subject) > filename
  print "knowledge_points:" > filename
  print sprintf("  - \"%s\"", kp) > filename
  print sprintf("question_type: \"%s\"", qtype) > filename
  print sprintf("difficulty: %d", difficulty) > filename
  print "source: \"408真题\"" > filename
  print sprintf("number: %d", int(qnum)) > filename
  print "---" > filename
  print "" > filename

  # Write question content (strip trailing whitespace)
  gsub(/\n+$/, "", qcontent)
  print qcontent > filename

  close(filename)
  printf "Created: %s\n", filename

  qnum = ""
  qcontent = ""
}
