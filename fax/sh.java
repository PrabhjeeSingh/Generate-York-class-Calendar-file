// import java.util.List;
// import java.util.Map;

// /*
// #Here is the input set of JSON data representing games:
// #
// #[
// #  { "home_team": "Raptors", "away_team": "Cavaliers", "winning_team": "Cavaliers" },
// #  { "home_team": "Cavaliers", "away_team": "Celtics", "winning_team": "Cavaliers" },
// #  { "home_team": "Celtics", "away_team": "Lakers", "winning_team": "Celtics" },
// #  { "home_team": "Cavaliers", "away_team": "Lakers", "winning_team": "Cavaliers" },
// #  { "home_team": "Celtics", "away_team": "Raptors", "winning_team": "Raptors" },
// #  { "home_team": "Lakers", "away_team": "Raptors", "winning_team": "Raptors" },
// #  { "home_team": "Celtics", "away_team": "Cavaliers", "winning_team": "Celtics" }
// #]
// #
// #We expect you to produce an output of standings records in the following JSON format:
// #
// #[
// #  { "team": "Raptors", "wins": 2, "losses": 1 },
// #  { "team": "Cavaliers", ... },
// #  { ... }
// #]
// */

// class Main {

//   static List<Map<String, String>> games = List.of(
//       Map.of("home_team", "Raptors", "away_team", "Cavaliers", "winning_team", "Cavaliers"),
//       Map.of("home_team", "Cavaliers", "away_team", "Celtics", "winning_team", "Cavaliers"),
//       Map.of("home_team", "Celtics", "away_team", "Lakers", "winning_team", "Celtics"),
//       Map.of("home_team", "Cavaliers", "away_team", "Lakers", "winning_team", "Cavaliers"),
//       Map.of("home_team", "Celtics", "away_team", "Raptors", "winning_team", "Raptors"),
//       Map.of("home_team", "Lakers", "away_team", "Raptors", "winning_team", "Raptors"),
//       Map.of("home_team", "Celtics", "away_team", "Cavaliers", "winning_team", "Celtics")
//   );


//   public static void main(String[] args) {
//     System.out.println(games);
//   }
// }