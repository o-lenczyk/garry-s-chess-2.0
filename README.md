# garry's chess 2.0

![](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/o-lenczyk/garry-s-chess-2.0/main/test-results/endpoint.json)

## goal
the goal is to reinvent chess. possible evolution to [fairy chess](https://en.wikipedia.org/wiki/Fairy_chess) or dungeon crawler

## gui
- [x] pygame
- [ ] cli

## what is working
- [ ] side to move
- [x] piece moves
- [x] piece captures
- [x] possible moves indicators
- [x] castling
- [ ] en passant
- [ ] promotion
- [ ] checks
- [ ] pin to king
- [ ] stealmate
- [ ] fifty move rule
- [ ] three repetitions rule
- [ ] tests
- [ ] [UCI](https://www.chessprogramming.org/UCI)

## how to run - linux
either:
- download pyinstaller executable (releases)
- download pyinstaller package with python and requirements installed
- clone repository and install requirements manually
  - `python3 -m pip install -r requirements.txt --user`  
  - run `main.py`

## how to run - windows
- clone the repository and install the requirements

## code formatter
black

## matrix opeterations
are explained in matrix jupyter notebook

## board representiation
hybrid (redutant solution) between piece-list and bitboard is used