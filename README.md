# Keras Docset for Zeal/Dash

## Dependencies
* You need to install [Dashing](https://github.com/technosophos/dashing)

```bash
go get -u github.com/technosophos/dashing
```


## Build
```bash
bash wget_html.sh # download a html
bash build.sh # preprocess & build dash docset

# Don't run unless the path is same
bash copy_docset.sh # copy the built docset to ~/.local/share/Zeal/Zeal/docsets/
```

## File
```text
.
├── build.sh
├── copy_docset.sh # check the path before you run this
├── dashing.json
├── README.md
├── theme.css
└── wget_html.sh
```

## Contributions
* Please feel free to send a PR