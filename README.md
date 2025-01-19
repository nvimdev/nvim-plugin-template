# nvim-plugin-template

Neovim plugin template; includes automatic documentation generation from README, integration tests with Busted, and linting with Stylua

## Usage

1. Click `use this template` button generate a repo on your github.
2. Clone your plugin repo. Open terminal then cd plugin directory.
3. Run `python3 rename.py your-plugin-name`. This will replace all `nvim-plugin-template` to your `plugin-name`. 
   Then it will prompt you input `y` or `n` to remove example codes in `init.lua` and
   `test/plugin_spec.lua`. If you are familiar this repo just input `y`. If you are looking at this template for the first time I suggest you inspect the contents. After this step `rename.py` will also auto-remove.

Now you have a clean plugin environment. Enjoy!

## Format

The CI uses `stylua` to format the code; customize the formatting by editing `.stylua.toml`.

## Test

See [Running tests locally](https://github.com/nvim-neorocks/nvim-busted-action?tab=readme-ov-file#running-tests-locally)

## CI

- Auto generates doc from README.
- Runs the [nvim-busted-action](https://github.com/nvim-neorocks/nvim-busted-action) for test.
- Lints with `stylua`.

## More

To see this template in action, take a look at my other plugins.

## License MIT
