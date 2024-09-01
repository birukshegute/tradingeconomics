use std::error::Error;

fn main() {
    let client = "guest:guest";
    let base = "http://api.tradingeconomics.com";
    let client_key:String  = String::from(client);
    let base_url:String = String::from(base);
	get_intraday_by_symbol(base_url, client_key);
    let client_key:String  = String::from(client);
    let base_url:String = String::from(base);
	get_intraday_by_date_time(base_url, client_key);
    let client_key:String  = String::from(client);
    let base_url:String = String::from(base);
	get_intraday_between_dates(base_url, client_key);

}

fn get_intraday_by_symbol(base_url:String, client_key:String) -> Result<(), Box<dyn Error>> {
    let path:String = String::from("/markets/intraday");
    let params:String = String::from("/aapl:us");
    let url = format!("{}{}{}?c={}&f=json", base_url, path, params, client_key);
    let resp = reqwest::blocking::get(url)?.json::<serde_json::Value>()?;
    println!("-----------------------Intraday for a single market----------------------");
    println!("{:#?}", resp);
    Ok(())

}

fn get_intraday_by_date_time(base_url:String, client_key:String) -> Result<(), Box<dyn Error>> {
    let path:String = String::from("/markets/intraday");
    let params:String = String::from("/aapl:us");
    let date:String = String::from("?d1=2017-08-10 15:30");
    let url = format!("{}{}{}{}&c={}&f=json", base_url, path, params, date, client_key);
    let resp = reqwest::blocking::get(url)?.json::<serde_json::Value>()?;
    println!("-----------------------Intraday by symbol date and time----------------------");
    println!("{:#?}", resp);
    Ok(())

}

fn get_intraday_between_dates(base_url:String, client_key:String) -> Result<(), Box<dyn Error>> {
    let path:String = String::from("/markets/historical");
    let params:String = String::from("/aapl:us");
    let date1:String = String::from("?d1=2017-08-01");
    let date2:String = String::from("&d2=2017-08-08");
    let url = format!("{}{}{}{}{}&c={}&f=json", base_url, path, params, date1, date2, client_key);
    let resp = reqwest::blocking::get(url)?.json::<serde_json::Value>()?;
    println!("-----------------------Intraday by symbol between dates----------------------");
    println!("{:#?}", resp);
    Ok(())

}
