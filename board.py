"""functions to set up and display the board"""
import conf
import piece
import helpers

starting_piece_order = [
    piece.Rook,
    piece.Knight,
    piece.Bishop,
    piece.Queen,
    piece.King,
    piece.Bishop,
    piece.Knight,
    piece.Rook,
]


def draw_board():
    # Give the surface a color to separate it from the background
    conf.square.fill(conf.SQUARE_COLOR)
    rect = conf.square.get_rect()

    for y_cord in range(0, 8):
        for x_cord in range(0, 8):
            if y_cord % 2 ^ x_cord % 2:
                conf.screen.blit(
                    conf.square,
                    [y_cord * (conf.SQUARE_SIZE), x_cord * (conf.SQUARE_SIZE)],
                )


def draw_pieces():
    for i in range(0, 8):
        conf.all_pieces.add(
            starting_piece_order[i](
                i * conf.SQUARE_SIZE, 0, "Black", conf.SQUARE_SIZE, i
            )
        )

    for i in range(0, 8):
        conf.all_pieces.add(
            piece.BlackPawn(
                i * conf.SQUARE_SIZE, conf.SQUARE_SIZE, "Black", conf.SQUARE_SIZE, i + 8
            )
        )

    for i in range(0, 8):
        conf.all_pieces.add(
            piece.WhitePawn(
                i * conf.SQUARE_SIZE,
                6 * conf.SQUARE_SIZE,
                "White",
                conf.SQUARE_SIZE,
                i + 48,
            )
        )

    for i in range(0, 8):
        conf.all_pieces.add(
            starting_piece_order[i](
                i * conf.SQUARE_SIZE,
                7 * conf.SQUARE_SIZE,
                "White",
                conf.SQUARE_SIZE,
                i + 56,
            )
        )

    conf.all_pieces.update()


def draw_legal_moves(legal_moves):
    for legal_move in legal_moves:
        conf.move_indicators.add(helpers.PossibleMoves(legal_move))

    conf.move_indicators.update()


def erase_legal_moves():
    conf.move_indicators.empty()
    conf.move_indicators.update()


def draw_legal_captures(legal_captures):
    for legal_capture in legal_captures:
        conf.move_indicators.add(helpers.PossibleCaptures(legal_capture))

    conf.move_indicators.update()
