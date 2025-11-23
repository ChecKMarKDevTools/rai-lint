export default {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'footer-max-line-length': [2, 'always', 100],
    'rai-footer-exists': [2, 'always'],
    'subject-case': [2, 'always', ['lower-case']],
  },
  plugins: ['@checkmark/commitlint-plugin-rai'],
};
