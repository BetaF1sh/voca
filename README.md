# voca-gorae

(WIP) 인쇄 가능한 [암기고래] 전용의 쪽지 시험 생성기

A printable vocabulary exam generator for [AmgiGorae][암기고래]

## Install

```
pip install voca-gorae
```

## How to use

```
voca 'wordlist' -s 'exam' -i 1 -w
```

### Requirement argument

`wordlist` is path of [`./wordlist.xlsx`](./wordlist.xlsx)

### optional arguments

- `-s`, `--save` where to save file. default is "exam"
- `-i` `--index` Set the parsing loction of columm
- `-w`, `--web` Show on web after save. You can view solution at `/a`

[암기고래]: https://play.google.com/store/apps/details?id=com.belugaedu.amgigorae
