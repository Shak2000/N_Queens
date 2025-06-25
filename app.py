from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from main import Board

chessboard = Board(8)
app = FastAPI()


@app.get("/")
async def get_ui():
    # Serve the HTML file at the root route
    return FileResponse('index.html')


@app.post("/create_board")
async def create_board(size: int = 1):
    # Mount static files (if you have CSS/JS files)
    # app.mount("/static", StaticFiles(directory="static"), name="static")
    global chessboard
    chessboard = Board(size)
    return chessboard.board

@app.get("/get_board")
async def get_board():
    return chessboard.board

@app.post("/set_queen")
async def set_queen(x: int, y: int):
    error_message = ("The input must consist of two integers from 0 (inclusive) to the board side length "
                   "(exclusive) at a location not attacked by any other queen.")

    try:
        if 0 <= x < chessboard.n and 0 <= y < chessboard.n and chessboard.is_safe(x, y):
            chessboard.board[x][y] = "Q"
            return {"success": True, "message": f"Queen placed at ({x}, {y})"}
        else:
            raise HTTPException(
                status_code=400,
                detail="Cannot place queen - position is attacked or out of bounds"
            )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@app.post("/remove_queen")
async def remove_queen(x: int, y: int):
    try:
        if 0 <= x < chessboard.n and 0 <= y < chessboard.n:
            chessboard.board[x][y] = "."
            return {"success": True, "message": f"Queen removed from ({x}, {y})"}
        else:
            raise HTTPException(
                status_code=400,
                detail="Position out of bounds"
            )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@app.post("/solve")
async def solve():
    return chessboard.solve_nqueens_once(0)
