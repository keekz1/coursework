<?php error_reporting(0); ?> 
<?php
    $errors = '';
    $myemail = "W1832388@my.westminster.ac.uk";

    if(empty($_POST["message"]))
    {
        $errors .= "\n Error: a Message is Required inorder to Submit";
    }
    $message = $_POST["message"];
    $enjoyability = $_POST["siteEnjoyabilityRange"];
    $used = $_POST["deviceUsed"];
    $Wanted = $_POST["deviceWanted"];

    if(empty($errors)){
        $email_subject = "User Comment";
        $email_body = "Your page has received a new comment. ".
        "\nThey gave the sit a scour of: $enjoyability".
        "\nThey used a $used device".
        "\nThey wanted to use a $Wanted device".
        "\nHere is what there comment said:\n$message";
        $headers = "From: User@email.address\n";
        mail($myemail, $email_subject,$email_body,$headers);
        header('Location: thankYouPage.html');
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comment Page</title>        
   
    <link rel="styleSheet" href="/CodeBank/LoginPages/CSS/sSLogInPage.css">
    <link rel="stylesheet" type="text/css" href="/CodeBank/SiteWideCSS/sSUnified.css"/>

</head>
    <body>

        <div class="spacerFrame"></div>
        <div class="galFrame">
            <div class="spaceFrame1"></div>
            <div class="spaceFrame2"></div>
            <div class="container">
                <form  name="notificationbot" action="Most notificationbot.php" onsubmit="return validateForm()" method="post">
                        <div class="frame1">
                            <p>How satisfied were you with our website today?</p>
                            <div class="controls">
                                <label class="radio"  for="1">1    
                                <input type="radio" id="1" name="siteEnjoyabilityRange" value="1">
                                </label>
                                <label class="radio" for="2">2
                                <input type="radio" id="2" name="siteEnjoyabilityRange" value="2">
                                </label>
                                <label class="radio" for="3">3
                                <input type="radio" id="3" name="siteEnjoyabilityRange" value="3">
                                </label>
                                <label class="radio" for="4">4
                                <input type="radio" id="4" name="siteEnjoyabilityRange" value="4">
                                </label>
                                <label class="radio" for="5">5
                                <input type="radio" id="5" name="siteEnjoyabilityRange" value="5">   
                                </label>     
                            </div>
                        </div>
                

                    <div id="moveFrame" class="worningFrame"></div>
                    <div id="worningborder" class="frame2">
                        <p>It would realy help us improve our site if you would leave us a short message on your Experience?</p>
                        <textarea id="myTextArea" name="message"></textarea>    
                    </div>
 
                    <div class="frame3">
                        <p>On What Device Did You Complete This Task Today? (optional)</p>
                        <select id="usedDevice" Name="deviceUsed">
                        <option value="">--please select--</option>
                        <option value="Phone">Phone</option>
                        <option value="Tablet">Tablet</option>
                        <option value="Windows">Windows</option>
                        <option value="Mac">Mac</option>
                        </select>
                    </div>
                    <div class="frame4">
                        <p>If you had to complete this task again, On What Device would you prefer to do it? (optional)</p>
                        <select id="wantedDevice" name="deviceWanted">
                        <option value="">--please select--</option>
                        <option value="Phone">Phone</option>
                        <option value="Tablet">Tablet</option>
                        <option value="Windows">Windows</option>
                        <option value="Mac">Mac</option>
                        </select>
                    </div>
                    <input class="subit" type="submit" value="Submit">

                </form>
            </div>
        </div>

        <script>
            function validateForm(){
                let x = document.forms["Most notificationbot"]["message"].value;
                if (x == "") {
                        var div = document.createElement("div");
                        div.style.width = "50vw";
                        div.style.height = "auto";
                        div.style.padding = "1vw";
                        div.style.margin = "1vw";
                        div.style.borderRadius ="5px";
                        div.style.background = "#CB4B15";
                        div.style.color = "#C5C3C0";
                        div.innerHTML = "A Message Is Required Inorder To Submit!!";
                        
                        document.getElementById("moveFrame").appendChild(div);
                        document.getElementById("worningborder").style.border = "1px  solid #CB4B15";
                        document.getElementById("myTextArea").placeholder = "A Message Is Required Inorder To Submit!!";
                        return false;
                        
                } 
                
            }
        </script>

    </body>
</html>
