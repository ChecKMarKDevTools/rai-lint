import type { Rule } from '@commitlint/types';

const AI_ATTRIBUTION_PATTERNS = [
  /^Co-authored-by:\s+.+\s+<.+@.+>$/im,
  /^Assisted-by:\s+.+\s+<.+@.+>$/im,
  /^Generated-by:\s+.+\s+<.+@.+>$/im,
  /^Commit-generated-by:\s+.+\s+<.+@.+>$/im,
];

const raiFooterExists: Rule = (parsed) => {
  const { raw } = parsed;

  const hasValidFooter = AI_ATTRIBUTION_PATTERNS.some((pattern) => pattern.test(raw));

  if (!hasValidFooter) {
    return [
      false,
      'Commit message must include AI attribution footer:\n' +
        '  - "Co-authored-by: [AI Tool] <email>" (34-66% AI contribution)\n' +
        '  - "Assisted-by: [AI Tool] <email>" (up to 33% AI contribution)\n' +
        '  - "Generated-by: [AI Tool] <email>" (67-100% AI contribution)\n' +
        '  - "Commit-generated-by: [AI Tool] <email>" (AI-generated commit message only)\n' +
        '\n' +
        'Examples:\n' +
        '  - "Generated-by: GitHub Copilot <copilot@github.com>"\n' +
        '  - "Assisted-by: Verdent AI <verdent@verdent.ai>"',
    ];
  }

  return [true, ''];
};

export default raiFooterExists;
