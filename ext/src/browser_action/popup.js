document.addEventListener("click", function(e) {
    let id = e.target.id;
    browser.tabs.query({active: true, currentWindow: true})
    .then(portmark(id))
    .catch(reportError);
});

/**
 * Just log the error to the console.
 */
function reportError(error) {
    console.error(`Could not porten: ${error}`);
}

function portmark(id) {
    var gettingActiveTab = browser.tabs.query({active: true, currentWindow: true});
    gettingActiveTab.then((tabs) => {
        var title = tabs[0].title;
        var url   = tabs[0].url;        

        data = new FormData()
        data.set('Title', title)
        data.set('Url', url)
        data.set('Cat', id)
        
        let request = new XMLHttpRequest();
        request.open("POST", 'http://localhost:5000/', true);
        request.send(data)

      });    

}