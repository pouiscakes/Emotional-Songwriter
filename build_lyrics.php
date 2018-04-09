<?php
  require 'redirect.php';

  session_save_path("/webpages/isantill/mcc/sessions");
  session_start(); // must start session before any HTML
?>

<?php
if (isset($_POST['selectedEmotion'])) {
  $_SESSION['emotion'] = $_POST['selectedEmotion'];
}
// user selected a lyric in build_lyrics
elseif (isset($_POST['selectedlyric'])) {
  // ensure session variables are initialized  
  if (!isset($_SESSION['lyrics'])) { 
    $_SESSION['lyrics'] = ""; 
    $_SESSION['checkRepeat'] = ""; 
  }

  // prevents duplicate lyrics added caused by refreshing page
  if ($_SESSION['checkRepeat'] != $_POST['selectedlyric']) { 
    $_SESSION['lyrics'] = $_SESSION['lyrics'] . $_POST['selectedlyric']; // add selected lyric to the lyrics
  }
  $_SESSION['checkRepeat'] = $_POST['selectedlyric']; // remember the most recently added lyrics
  
  echo '<div class="rightcolumn displayLyrics">' . $_SESSION['lyrics'] . '</div>';

}

elseif (isset($_POST['custom'])) {
  // ensure session variables are initialized  
  if (!isset($_SESSION['lyrics'])) { 
    $_SESSION['lyrics'] = ""; 
    $_SESSION['checkRepeat'] = ""; 
  }

  // prevents duplicate lyrics added caused by refreshing page. CAVEAT here is that user can't enter duplicate custom lines back to back
  if ($_SESSION['checkRepeat'] != $_POST['customLyric']) { 
    if ($_POST['customLyric'] != ""){ // prevent from adding lyrics if custom lyrics are empty string
      $_SESSION['lyrics'] = $_SESSION['lyrics'] . $_POST['customLyric'] . '<br>'; // add selected lyric to the lyrics
    }
  }
  $_SESSION['checkRepeat'] = $_POST['customLyric']; // remember the most recently added lyrics
  
  echo '<div class="rightcolumn displayLyrics">' . $_SESSION['lyrics'] . '</div>';
}

// do nothing, just regenerates lyrics 
elseif (isset($_POST['regenerate'])) {
  // ensure session variables are initialized  
  if (!isset($_SESSION['lyrics'])) { 
    $_SESSION['lyrics'] = ""; 
    $_SESSION['checkRepeat'] = ""; 
  }
  echo '<div class="rightcolumn displayLyrics">' . $_SESSION['lyrics'] . '</div>';
}
// redirect user to finish page
elseif (isset($_POST['finished'])) {
    $_SESSION['finished'] = 1;
    redirect("finish_song.php");
}

elseif(!isset($_GET['data'])) {
  unset($_SESSION['lyrics']);
}

elseif(isset($_GET['data'])){
  if(isset($_SESSION['lyrics'])){
    unset($_GET['backToBuild']);
    echo '<div class="rightcolumn displayLyrics">' . $_SESSION['lyrics'] . '</div>';
  }
}

else{
  unset($_SESSION['lyrics']);
}

?> 

<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Build Lyrics</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/bootstrap.css" rel="stylesheet" media="screen">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">


    <link href="css/mcc_style.css" rel="stylesheet" media="screen">
    <link href='https://fonts.googleapis.com/css?family=Montserrat:100,200,300,400,500,600,700,800,900' rel='stylesheet'>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js">
    <script type="text/javascript">
    </script>
  </head>
  <body onload="$('html, body').animate({ scrollTop: $(document).height() }, 1000);">
    <div class="wholepage" id="startHere">
      <a style="display:block height:100%" href="select_emotion.php">
        <div class="leftcolumn">
          <span class="leftcolumntext">Current Feeling:</span> 
          <?php
          echo '<img src="images/feeling_' . $_SESSION['emotion'] . '.jpeg" alt="' . $_SESSION['emotion'] . '">';
          ?>
          <!-- <img src="images/feeling_sadness.jpeg" alt="sadness"> -->
        </div>
      </a>
      <div class="rightcolumn">
        <h1 class="heading">Suggested Lyrics</h1>
        <div class="add_course_form" id="add_course_form" >
        <form action="" method="post" >

          <!-- set default enter button behavior -->
          <button style="overflow: visible !important; height: 0 !important; width: 0 !important; margin: 0 !important; border: 0 !important; padding: 0 !important; display: block !important;" type="submit" name="custom"/>

        <?php
          $lyrics = file('lyrics/rhymed_lyrics_' . $_SESSION['emotion'] . '.txt', FILE_IGNORE_NEW_LINES);
          // $lyrics = file('lyrics/rhymed_lyrics_sadness.txt', FILE_IGNORE_NEW_LINES);
          $lyrics_size = sizeof($lyrics);

          for ($i = 0; $i < 3; $i++) {
            $offset = 3 * mt_rand(0, $lyrics_size/3 - 1);
            $line1 = $lyrics[$offset];
            $line2 = $lyrics[$offset + 1];
            echo '<button type="submit" class="lyricbox" name="selectedlyric" value="' . $line1 . '<br>' . $line2 . '<br>"><div>' . $line1 . '</div><div class="secondlyricline">' . $line2 . '</div></button><br>';
          }
        ?>

          <!-- <div class="customLyric"> Or </div> -->
          <div class="customLyric">
            Write your own <input type="text" name="customLyric">
            <button type="submit" class="customLyricbox" name="custom">Use this Lyric</button><br>
          </div>

          <button type="submit" name="regenerate" class="button-control"><span class="glyphicon glyphicon-refresh"></span> &nbsp;&nbsp;Regenerate Lyrics</button><br>
          <button type="submit" name="finished" class="button-control"><span class="glyphicon glyphicon-ok"></span> &nbsp;&nbsp;Finish Song</button>
        </form>
      </div>
    </div> 
  </body>
</html>

