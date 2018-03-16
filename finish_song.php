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
    <a style="display:block height:100%" href="http://students.engr.scu.edu/~isantill/mcc/build_lyrics.php">
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
            
            echo '<button type="submit" class="lyricbox"><div>';  

            if(!isset($_SESSION['lyrics'])){
              echo "something is wrong here";
            }
            else {
              $lyrics_split = explode("<br>", $_SESSION['lyrics']); // split up <br>'s inside the lyrics session variable
              echo "<div>" . $lyrics_split[0] . "</div>";
              for ($i = 1; $i < sizeof($lyrics_split); $i++) {
                echo '<div class="secondlyricline">' . $lyrics_split[$i] . '</div>';
              }
            }
            echo '</div></button><br>';
            
            
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

