function startSpeech() {

    alert("Recording started");

    const SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;

    const recognition = new SpeechRecognition();

    recognition.lang = "en-US";

    recognition.start();

    recognition.onresult = function(event) {

        alert("Voice detected");

        const text = event.results[0][0].transcript;

        alert(text);

        document.getElementById("answer").value = text;
    };

    recognition.onerror = function(event) {

        alert("Error: " + event.error);
    };
}