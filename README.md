# lsub

Combines the powers of:

- [ripgrep](https://www.github.com/BurntSushi/ripgrep)
- [ripgrepy](https://github.com/securisec/ripgrepy)
- [questionary](https://www.github.com/tmbo/questionary)

to replace occurrences of specified regex needle with a replacement.
Asks confirm for each replacement.

Example:

1. Create three files

```

$ echo "Hello world!" > anyfile.txt
$ echo "The world is not enough" > anyfile2.txt
$ echo "The wooooorld's on fire!" > anyfile3.txt

```

2. Find the `w*rld` inside of it

```
$ rg "w\w+rld"
anyfile3.txt
1:The wooooorld's on fire!

anyfile.txt
1:Hello world!

anyfile2.txt
1:The world is not enough

```

3. Replace the `w*rld` with the whole `universe`

```
$ lsub "w\w+rld" "universe"

./anyfile2.txt
000001:The world is not enough
Replace with "universe"? (n)ext/next (f)ile/(r)eplace/replace (a)ll/(q)uit > r

./anyfile3.txt
000001:The wooooorld's on fire!
Replace with "universe"? (n)ext/next (f)ile/(r)eplace/replace (a)ll/(q)uit > r

./anyfile.txt
000001:Hello world!
Replace with "universe"? (n)ext/next (f)ile/(r)eplace/replace (a)ll/(q)uit > n
```

4. See the changes you want, reflected in the filesystem!

```
$ rg "w\w+rld"
anyfile.txt
1:Hello world!

$ rg "universe"
anyfile2.txt
1:The universe is not enough

anyfile3.txt
1:The universe's on fire!
```


Help message:

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
