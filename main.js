const webdriver = require('selenium-webdriver');
const clearCache = require('selenium-chrome-clear-cache');
const websites = 
["https://netflix.com","https://apple.com","https://homedepot.com","https://mail.yahoo.com","https://cnn.com"
,"https://etsy.com","https://yahoo.com","https://indeed.com"
,"https://target.com","https://microsoft.com","https://nytimes.com","https://mayoclinic.org","https://espn.com"
,"https://usps.com","https://quizlet.com","https://gamepedia.com"
,"https://lowes.com","https://merriam-webster.com","https://steampowered.com","https://mapquest.com"
,"https://foxnews.com","https://allrecipes.com","https://quora.com","https://aol.com"
,"https://britannica.com","https://live.com","https://bestbuy.com","https://rottentomatoes.com"
,"https://play.google.com","https://cnet.com","https://roblox.com","https://usnews.com","https://zillow.com"
,"https://businessinsider.com","https://bulbagarden.net","https://paypal.com","https://finance.yahoo.com"
,"https://genius.com","https://usatoday.com"
,"https://realtor.com","https://medicalnewstoday.com","https://fedex.com","https://bankofamerica.com","https://washingtonpost.com"
,"https://investopedia.com","https://speedtest.net","https://spotify.com","https://cdc.gov","https://chase.com"
,"https://hulu.com","https://xfinity.com","https://msn.com","https://dictionary.com"
,"https://weather.com","https://ups.com","https://verizon.com","https://forbes.com","https://wowhead.com"
,"https://expedia.com","https://urbandictionary.com"
,"https://foodnetwork.com","https://nbcnews.com","https://macys.com","https://apartments.com","https://ign.com"
,"https://capitalone.com","https://costco.com","https://theguardian.com"
,"https://cnbc.com","https://glassdoor.com","https://yellowpages.com","https://att.com","https://bbc.com"
,"https://khanacademy.org","https://ny.gov","https://twitch.tv","https://adobe.com","https://cbssports.com","https://google.com","https://ynet.co.il","https://en.wikipedia.org","https://youtube.com"
,"https://amazon.com","https://facebook.com","https://twitter.com","https://fandom.com","https://pinterest.com"
,"https://imdb.com","https://reddit.com","https://yelp.com"
,"https://instagram.com","https://ebay.com","https://walmart.com","https://craigslist.org","https://healthline.com"
,"https://tripadvisor.com","https://linkedin.com","https://webmd.com"]

function hodl(ms){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve();
        ;} , ms
        );
    });
}
const surf = async() => {
    const driver = await new webdriver.Builder().forBrowser('chrome').build();
    console.log("starting surfing, make sure you'r sniffing!")
    await clearCache({webdriver, driver},{cookies: true},{cache: true},{history: true});
    hodl(3000)
    try{
        for(const address of websites){
            console.log("surfing to "+ address);
            await hodl(5000);
            await driver.get(address);
        }
        await driver.quit();   
    }catch (error){
        console.log(error)
    }
    console.log("over and out.")
};
surf()