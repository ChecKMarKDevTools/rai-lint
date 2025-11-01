import type { Plugin } from '@commitlint/types';
import raiFooterExists from './rules/rai-footer-exists';

const plugin: Plugin = {
  rules: {
    'rai-footer-exists': raiFooterExists,
  },
};

export default plugin;
