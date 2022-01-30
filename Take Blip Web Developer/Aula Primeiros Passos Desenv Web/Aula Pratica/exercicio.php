<html>
	<head>
		<title>Meu primeiro site em PHP! Woohoo!</title>
        <link rel="stylesheet" href="//code.jquery.com/ui/1.13.1/themes/base/jquery-ui.css">
        <link rel="stylesheet" href="/resources/demos/style.css">
        <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
        <script src="https://code.jquery.com/ui/1.13.1/jquery-ui.js"></script>
	</head>
	<body>
	    <div id="accordion">
            <h3>Pg 1</h3>
            <div>
                <p>
                    Voce abriu pagina 1.
                </p>
            </div>
            <h3>Pg 2</h3>
            <div>
                <p>
                    Voce abriu pagina 2.
                </p>
            </div>
            <h3>Pg 3</h3>
            <div>
                <p>
                    Voce abriu pagina 3.
                </p>
            </div>
        </div>
	</body>
    
    <script>
        $( function() {
            $("#accordion").accordion();
        });
    </script>
</html>