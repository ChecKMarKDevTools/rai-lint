import type { Rule } from '@commitlint/types';

const RAI_FOOTER_PATTERNS = [
  /^🛡️\s+RAI:\s+AI-Generated$/im,
  /^🛡️\s+RAI:\s+AI-Assisted$/im,
  /^Generated-by:\s+Verdent AI\s+<verdent@verdent\.ai>$/im,
];

const raiFooterExists: Rule = (parsed) => {
  const { raw } = parsed;

  const hasValidFooter = RAI_FOOTER_PATTERNS.some((pattern) => pattern.test(raw));

  if (!hasValidFooter) {
    return [
      false,
      'Commit message must include a valid RAI footer:\n' +
        '  - "🛡️ RAI: AI-Generated"\n' +
        '  - "🛡️ RAI: AI-Assisted"\n' +
        '  - "Generated-by: Verdent AI <verdent@verdent.ai>"',
    ];
  }

  return [true, ''];
};

export default raiFooterExists;
