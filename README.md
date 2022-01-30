# garry's chess 2.0

![](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/o-lenczyk/garry-s-chess-2.0/master/test-results/endpoint.json) ![](https://img.shields.io/github/v/release/o-lenczyk/garry-s-chess-2.0)

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
- [x] autopromotion to queen
- [ ] promotion to other pieces
- [ ] en passant
- [x] checks
- [x] pin to king
- [ ] stealmate
- [ ] fifty move rule
- [ ] three repetitions rule
- [ ] algebraic notation
- [ ] load from [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation)
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