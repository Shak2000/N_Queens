# N-Queens Solver

A beautiful, interactive web-based N-Queens puzzle solver with a modern UI. This application allows users to manually place queens on a chessboard and then solve the remaining puzzle using an intelligent backtracking algorithm.

## Features

- 🎯 **Interactive Chess Board**: Click on squares to place or remove queens
- 🧠 **Smart Solver**: Continues from your current board state instead of starting over
- 📏 **Customizable Board Size**: Support for boards from 1×1 to 12×12
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations
- 📱 **Responsive Design**: Works on desktop and mobile devices
- ⚡ **Real-time Validation**: Prevents invalid queen placements
- 🔄 **Partial Solutions**: Solve from any valid starting position

## How It Works

The N-Queens problem is a classic computer science puzzle where you must place N queens on an N×N chessboard such that no two queens attack each other. Queens can attack horizontally, vertically, and diagonally.

This solver uses a **backtracking algorithm** that:
1. Validates your current queen placements
2. Continues solving from your partial solution
3. Finds a complete solution or reports if none exists

## Project Structure

```
n-queens-solver/
├── main.py          # Core N-Queens solving logic
├── app.py           # FastAPI backend server
├── index.html       # Frontend web interface
└── README.md        # This file
```

## Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install required dependencies**:
   ```bash
   pip install fastapi uvicorn
   ```

3. **Start the server**:
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:8000
   ```

## Usage

### Basic Controls

- **Board Size**: Enter a number (1-12) and click "Create Board"
- **Place Queens**: Click on any square to place or remove a queen
- **Clear Board**: Remove all queens and start fresh
- **Solve**: Find a solution continuing from your current setup

### Interactive Features

1. **Manual Placement**: Click squares to place queens manually
2. **Validation**: The system prevents invalid placements (queens that would attack each other)
3. **Partial Solving**: Place some queens yourself, then let the algorithm complete the puzzle
4. **Visual Feedback**: Hover effects and status messages guide your interaction

### Example Workflow

1. Create an 8×8 board
2. Place a queen at position (0,1) by clicking that square
3. Place another queen at (2,3)
4. Click "Solve" to complete the remaining positions
5. The solver will find a valid solution that includes your placed queens

## API Endpoints

The FastAPI backend provides these endpoints:

- `GET /` - Serves the web interface
- `POST /create_board?size={n}` - Create a new n×n board
- `GET /get_board` - Get current board state
- `POST /set_queen?x={row}&y={col}` - Place a queen (if valid)
- `POST /remove_queen?x={row}&y={col}` - Remove a queen
- `POST /solve` - Solve from current board state

## Algorithm Details

### Backtracking Approach

The solver uses an enhanced backtracking algorithm:

1. **Validation**: Checks if current board state is valid
2. **Row-by-row solving**: Places one queen per row
3. **Constraint checking**: Ensures no queens attack each other
4. **Backtracking**: Undoes moves when no valid placement exists
5. **Optimization**: Skips rows that already contain user-placed queens

### Safety Checking

The `is_safe()` method checks:
- Column conflicts (vertical attacks)
- Diagonal conflicts (both diagonals)
- Row conflicts (handled by algorithm structure)

## Technical Details

### Frontend (index.html)
- Pure HTML/CSS/JavaScript
- Modern CSS with gradients and animations
- Responsive design with media queries
- Fetch API for backend communication

### Backend (app.py)
- FastAPI framework for REST API
- CORS enabled for development
- Global board state management
- Error handling with HTTP status codes

### Core Logic (main.py)
- Object-oriented Board class
- Recursive backtracking solver
- Board validation methods
- Multiple solution finding capability

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Known Limitations

- Board sizes above 12×12 may have performance issues
- No solution exists for 2×2 and 3×3 boards (this is mathematically correct)
- Single-threaded solving (one request at a time)

## Contributing

Feel free to contribute improvements:

1. Fork the project
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Potential Enhancements

- [ ] Multiple solution display
- [ ] Solution animation
- [ ] Undo/Redo functionality
- [ ] Save/Load board states
- [ ] Performance optimizations for larger boards
- [ ] Solution step-by-step visualization

## License

This project is open source and available under the MIT License.

## Troubleshooting

### Common Issues

**Server won't start:**
- Ensure Python 3.7+ is installed
- Install FastAPI: `pip install fastapi uvicorn`
- Check if port 8000 is available

**Frontend won't load:**
- Verify the server is running on `http://localhost:8000`
- Check browser console for JavaScript errors
- Ensure CORS is properly configured

**Solver seems slow:**
- Large board sizes (10+) naturally take longer
- Complex partial solutions may require more computation
- Consider reducing board size for faster results

**Queens disappear after clicking solve:**
- This is normal - the solver replaces your partial solution with a complete one
- Use "Clear Board" to start fresh if needed

## Contact

For questions, suggestions, or bug reports, please create an issue in the project repository.
