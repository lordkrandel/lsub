# lsub

Combines the powers of:

- [ripgrep](https://www.github.com/BurntSushi/ripgrep)
- [ripgrepy](https://github.com/securisec/ripgrepy)
- [questionary](https://www.github.com/tmbo/questionary)

to replace occurrences of specified regex needle with a replacement.

Asks confirm for each replacement.

```
$ lsub --help
Usage: lsub [OPTIONS] NEEDLE REPLACEMENT

Arguments:
  NEEDLE       [required]
  REPLACEMENT  [required]

Options:
  --path TEXT  [default: .]
  --help       Show this message and exit.
```

![immagine](https://user-images.githubusercontent.com/1665365/178082508-308be6eb-537a-45fc-ad01-7b757a0af9b0.png)
