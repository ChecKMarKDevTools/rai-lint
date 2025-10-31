import type { Rule } from '@commitlint/types';

const AI_ATTRIBUTION_PATTERNS = [
  /^Authored-by:\s+.+\s+<.+@.+>$/im,
  /^Commit-generated-by:\s+.+\s+<.+@.+>$/im,
  /^Assisted-by:\s+.+\s+<.+@.+>$/im,
  /^Co-authored-by:\s+.+\s+<.+@.+>$/im,
  /^Generated-by:\s+.+\s+<.+@.+>$/im,
];

const raiFooterExists: Rule = (parsed) => {
  const { raw } = parsed;

  const hasValidFooter = AI_ATTRIBUTION_PATTERNS.some((pattern) => pattern.test(raw));

  if (!hasValidFooter) {
    return [
      false,
      'Commit message must include AI attribution footer:\n' +
        '  1. "Authored-by: [Human] <email>" - Human only, no AI\n' +
        '  2. "Commit-generated-by: [AI Tool] <email>" - Trivial AI (docs, commit msg, advice)\n' +
        '  3. "Assisted-by: [AI Tool] <email>" - AI helped, but primarily human code\n' +
        '  4. "Co-authored-by: [AI Tool] <email>" - Roughly 50/50 AI and human (40-60 leeway)\n' +
        '  5. "Generated-by: [AI Tool] <email>" - Majority of code was AI generated\n' +
        '\n' +
        'Examples:\n' +
        '  - "Authored-by: Jane Doe <jane@example.com>"\n' +
        '  - "Commit-generated-by: ChatGPT <chatgpt@openai.com>"\n' +
        '  - "Assisted-by: GitHub Copilot <copilot@github.com>"\n' +
        '  - "Co-authored-by: Verdent AI <verdent@verdent.ai>"\n' +
        '  - "Generated-by: GitHub Copilot <copilot@github.com>"',
    ];
  }

  return [true, ''];
};

export default raiFooterExists;
