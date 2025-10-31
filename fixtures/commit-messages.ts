export const validCommitMessages = [
  'feat: add new feature\n\n🛡️ RAI: AI-Generated',
  'fix: resolve critical bug\n\n🛡️ RAI: AI-Assisted',
  'chore: update dependencies\n\nGenerated-by: Verdent AI <verdent@verdent.ai>',
  'docs: update README\n\nSome description\n\n🛡️ RAI: AI-Generated',
  'refactor: improve code quality\n\n🛡️ rai: ai-assisted',
];

export const invalidCommitMessages = [
  'feat: add new feature',
  'fix: resolve bug\n\nSome footer',
  'chore: update deps\n\n🛡️ RAI: Invalid',
  'docs: update\n\nGenerated-by: Someone Else',
];
