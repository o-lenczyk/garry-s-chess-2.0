# garry's chess 2.0

![](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/o-lenczyk/garry-s-chess-2.0/main/test-results/endpoint.json)

## goal
The goal is to reinvent chess. Possible evolution to [fairy chess](https://en.wikipedia.org/wiki/Fairy_chess) or dungeon crawler.

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

## install requirements
`python3 -m pip install -r requirements.txt --user`

## start
run `main.py`

## code formatter
black

## matrix opeterations
are explained in matrix jupyter notebook

## board representiation
Hybrid (redutant solution) between piece-list and bitboard is used