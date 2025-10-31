import type { Plugin } from '@commitlint/types';
import raiFooterExists from './rules/rai-footer-exists.js';

const plugin: Plugin = {
  rules: {
    'rai-footer-exists': raiFooterExists,
  },
};

export default plugin;
