# Keras Docset for Zeal/Dash
* Linux/Windows: [Zeal](https://zealdocs.org/)
* OSX: [Dash](https://kapeli.com/dash)

Not being update

## Screenshot
![zeal](assets/keras.dense.zeal.png)

## FEED URL
* Add `http://ocf.io/kkweon/docset/Keras.xml` to the feed url in Dash/Zeal

## Dependencies
* You need to install [Dashing](https://github.com/technosophos/dashing)

```bash
go get -u github.com/technosophos/dashing
```

## Build
```bash
make build
```

## Install
### Dash
- There is a keras.docset inside `keras.io`
- Preferences -> Docsets -> Add docset

### Zeal
- `keras.docset` to `~/.local/share/Zeal/Zeal/docsets/keras.docset`
`

## Files
```text
.
├── build.sh
├── copy_docset.sh # check the path before you run this
├── Makefile
├── dashing.json
├── README.md
├── theme.css
├── theme_extra.css
└── wget_html.sh
```

## Contributions
* Please feel free to send a PR
