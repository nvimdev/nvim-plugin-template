# nvim-plugin-template

A template repository for neovim plugins. Includes automatic doc generation based on your project's README, integration tests with Busted, and linting via Stylua.

## Usage

1. Click `use this template` button generate a repo under your github account.
2. Clone the newly-created repository, open a terminal, and cd to the plugin directory.
3. Run `python3 rename.py your-plugin-name`. This will:
    1. Replace all occurrences of `nvim-plugin-template` with `your-plugin-name`.
    2. Promt you for `y` or `n` to remove example code in `init.lua` and `test/plugin_spec.lua`.
        - If you are familiar with this repo, just select `y`.
        - Otherwise, I suggest you inspect the contents of thses files first.
    3. Lastly, `rename.py` will auto-remove itself.

Now you have a clean plugin development environment. Enjoy!

## Format

The CI uses `stylua` to format the code. Customize the formatting by editing `.stylua.toml`.

## Test

See [running tests locally](https://github.com/nvim-neorocks/nvim-busted-action?tab=readme-ov-file#running-tests-locally).

## CI

- Auto-generates doc from README.
- Runs the [nvim-busted-action](https://github.com/nvim-neorocks/nvim-busted-action) for tests.
- Lints with `stylua`.

## More

To see this template in action, take a look at my other plugins.

## License: MIT
