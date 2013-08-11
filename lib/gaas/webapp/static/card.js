function drawCard(game, deck) {
    $.ajax({
      type: "POST",
      url: "/api/v1/game/" + game + "/play",
      data: {"deckNum": deck},
      success: alertData,
      dataType: "json",
    });
}

function alertData(data) {
    $('div#intro').hide();
    if ( data < 0 ) {
        $('div#winnings').contents().replaceWith("You just lost " + Math.abs(data) + " bucks.");
    } else {
        $('div#winnings').contents().replaceWith("You just won " + Math.abs(data) + " bucks.");
    }
}

