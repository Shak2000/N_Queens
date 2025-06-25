from fastapi import FastAPI, HTTPException

from main import Board

chessboard = Board(8)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/create_board")
async def create_board(size: int = 1):
    global chessboard
    chessboard = Board(size)
    return chessboard.board


@app.get("/get_board")
async def get_board():
    return chessboard.board


@app.post("/set_queen")
async def set_queen(x, y):
    error_message = ("The input must consist of two integers from 0 (inclusive) to the board side length "
                     "(exclusive) at a location not attacked by any other queen.")

    try:
        x = int(x)
        y = int(y)

        if 0 <= x < chessboard.n and 0 <= y < chessboard.n and chessboard.is_safe(x, y):
            chessboard.board[x][y] = "Q"
            return True
        raise HTTPException(
            status_code=400,
            detail="Bad Request",
            headers={"Error": error_message}
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail="Bad Request",
            headers={"Error": error_message}
        )


@app.post("/remove_queen")
async def remove_queen(x, y):
    error_message = ("The input must consist of two integers from 0 (inclusive) to the board side length "
                     "(exclusive) at a location not attacked by any other queen.")

    try:
        x = int(x)
        y = int(y)

        if 0 <= x < chessboard.n and 0 <= y < chessboard.n and chessboard.is_safe(x, y):
            chessboard.board[x][y] = "."
            return True
        raise HTTPException(
            status_code=400,
            detail="Bad Request",
            headers={"Error": error_message}
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail="Bad Request",
            headers={"Error": error_message}
        )


@app.post("/solve")
async def solve():
    return chessboard.solve_nqueens_once(0)
