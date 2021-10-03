public class YourEvaluator extends Evaluator {

    // Implement your heuristic evaluation function here!
    // The below default function prefers:
    //  * not to lose (white king is worth at lot)
    //  * to win (black not having a king is worth a lot)
    //  * to have more white pieces (+1) and less black pieces (-1)

	public double eval(Position p) {
		double ret = 0;
		double dist=0;
		double multiplier=1;
		int empty=0;
		// for(int x = 0; x < p.board.length; ++x) {
		// 	for(int y = 0; y < p.board[x].length; ++y) {
		// 		if(p.board[x][y] == '.');
		// 			// System.out.println("empty");
		// 			empty++;
		// 	}
		// }
		for(int x = 0; x < p.board.length; ++x) {
			double x_dist=Math.abs(2.5-x);
			for(int y = 0; y < p.board[x].length; ++y) {
				multiplier=1;
				if (empty<32) {
					double y_dist=Math.abs(2.5-y);
					dist=x_dist+y_dist; // value between 1 and 5
					if (dist <= 1) multiplier=1.1;
					if (dist >1 && dist<=2) multiplier=1.06;
					if (dist >2 && dist<=3) multiplier=1.03;
					if (dist >3 && dist<=4) multiplier=1.01;
					if (dist > 4) multiplier=1;

				}
			
				if(p.board[x][y] == Position.Empty) continue;
				if(p.board[x][y] == Position.WKing) ret += 1e9;
				if(p.board[x][y] == Position.WQueen) ret += 9*multiplier;
				if(p.board[x][y] == Position.WRook) ret += 5;
				if(p.board[x][y] == Position.WBishop) ret += 3*multiplier;
				if(p.board[x][y] == Position.WKnight) ret += 3*multiplier;
				if(p.board[x][y] == Position.WPawn) ret += 1*multiplier;
				if(p.board[x][y] == Position.BKing) ret -= 1e9;
				if(p.board[x][y] == Position.BQueen) ret -= 9*multiplier;
				if(p.board[x][y] == Position.BRook) ret -= 5;
				if(p.board[x][y] == Position.BBishop) ret -= 3*multiplier;
				if(p.board[x][y] == Position.BKnight) ret -= 3*multiplier;
				if(p.board[x][y] == Position.BPawn) ret -= 1*multiplier;
			}
		}

		return ret;
	}
}
