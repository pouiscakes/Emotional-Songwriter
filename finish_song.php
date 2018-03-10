<?php
  require 'redirect.php';

  session_save_path("/webpages/isantill/mcc/sessions");
  session_start(); // must start session before any HTML
  if(!isset($_SESSION['finished'])){
    redirect("build_lyrics.php");
  }
?>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Build Lyrics</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/bootstrap.css" rel="stylesheet" media="screen">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/bootstrap.css" rel="stylesheet" media="screen">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link href="css/mcc_style.css" rel="stylesheet" media="screen">
    <link href='https://fonts.googleapis.com/css?family=Montserrat:100,200,300,400,500,600,700,800,900' rel='stylesheet'>

  </head>
  <body>
  <div class="wholepage">
    <a style="display:block height:100%" href="http://louisrlin.com">
      <div class="leftcolumn">
        <span class="leftcolumntext">You selected:</span> 
        <img src="images/feeling_sadness.jpeg" alt="sadness">
      </div>
    </a>
    <div class="rightcolumn">
      <h1 class="heading">Finished Song</h1>
      <div class="add_course_form" id="add_course_form" >
        <form action=<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?> method="post" >
          <?php
            $lyrics = file('lyrics/rhymed_lyrics_sadness.txt', FILE_IGNORE_NEW_LINES);
            $lyrics_size = sizeof($lyrics);
            // echo $lyrics_size;
            for ($i = 0; $i < 1; $i++) {
              $offset = 3 * mt_rand(0, $lyrics_size/3 - 1);
              $line1 = $lyrics[$offset];
              $line2 = $lyrics[$offset + 1];
              echo '<button type="submit" class="lyricbox"><div>' . $line1 . '</div><div class="secondlyricline">' . $line2 . '</div></button><br>';
            }
          ?>
        </form>
      <audio class="playback" controls autoplay="true">
          <source src="music/sadProgression.wav" type="audio/wav">
      </audio>
      <form action=<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?> method="post" >
        <button type="submit" class="button-control" onclick="alert('Hello World!')">Save Song</button>
      </form>
      </div>
    </div>
  </div>

  </body>
</html>

