Feature: User plays by rule
Scenario Outline: Dealer plays by the rules
  Given a hand <total>
   when the dealer determines a play
   then the <play> is correct

  Examples: Hands
  | total  | play   |
  | 10     | hit    |
  | 15     | hit    |
  | 16     | hit    |
  | 17     | stand  |
  | 18     | stand  |
  | 19     | stand  |
  | 20     | stand  |
  | 21     | stand  |
  | 22     | stand  |