# nvim-plugin-template
neovim plugin template integration test and doc publish

## Usage

click `use this template` button generate a repo on your github. then clone your plugin repo.open 
terminal then cd plugin directory , run `python3 rename.py your-plugin-name` this will replace all
`nvim-plugin-template` to your `pluing-name`. Then develope your plugin. Enjoy!

## Format

format use `stylua` and provide `.stylua.toml`.

## Test
use vusted for test install by using `luarocks --lua-version=5.1 install vusted` then run `vusted test`
for your test cases.

create test case in test folder file rule is `foo_spec.lua` with `_spec` more usage please check
[busted usage](https://lunarmodules.github.io/busted/)

## Ci
Ci support auto generate doc from README and integration test and lint check by `stylua`.


## More
Other usage you can look at my plugins

## License MIT
