# MUSIC SALES ANALYSIS

### OBJECTIVE - 
This project dives deep into music sales data to uncover key insights into customer purchasing behavior. My primary goal was to analyze sales performance based on customer demographics, geographic locations (cities and countries), and to identify which music genres or artists resonate most with specific customer segments. By leveraging this data, we aim to provide actionable intelligence for strategic business decisions and enhanced sales.

### ABOUT DATASET - 
"Sourced from a GitHub repository, the Music_analysis database is structured with multiple interconnected schemas. These include album, artist, customer, employee, genre, invoice, invoice_line, media_type, playlist_playlist_track, and track."

The music sales schemas along with their relation -

![458007161-01ca0883-f6b2-4822-8d9c-c2404ce52dff](https://github.com/user-attachments/assets/6958edd2-8528-4c40-a678-092c3eefc14a)

### GOALS -
The objective is to ascertain the leading musical artists within each distinct country, further segmented by their dominant genres, as determined by cumulative sales figures or streaming volumes. This granular, country-by-country and genre-specific artist popularity data will serve as a foundational insight for strategically enhancing song sales through precisely tailored promotional activities directed at identified target markets.

KEY QUESTION EXPLORED - 
1. Who is the senior most employee based on the job title?
2. Which countries have the most Invoices?
3. Which track love's the customer more than other?
4. What are top 3 values of total Invoices?
5. Which city has the best customer?
6. Who is the the best customer?
7. Return the details of the customer who loves the "Rock" music?
8. Return the details of the artist who have written the most "Rock" music?
9. Return the track name and duration that have a longest duration?
10. Most popular genre of the customer?

### TECHOLOGY USED - 
1. Python
2. postgreSQL
3. Python connector

### INSIGHTS / RESULT - 
1 .In today's globalized soundscape, there's no denying that hip-hop culture has become a pervasive force, its beats and rhymes echoing from every corner of the world. It's a vibrant, ever-evolving genre that has captured the hearts and minds of millions, influencing everything from fashion to language.
However, rewind to the 1970s, and you'd find a starkly different musical landscape dominating the airwaves and concert halls. This was the undisputed zenith of rock music. From stadium-filling anthems to raw, rebellious punk, rock was the pulsating heartbeat of a generation. Legendary bands and iconic guitar riffs defined an era, making it the supreme cultural touchstone. The sheer energy and diverse subgenres of rock at its peak left an indelible mark, shaping youth culture and challenging norms in a way that resonates even today.

![Code_Generated_Image](https://github.com/user-attachments/assets/dde9f5cb-ea1e-4f75-a5e1-7f49450a2508)

2. Mohan Madan occupied the distinguished position of the most senior employee in the music industry, designated at the L7 level.

![senior_employee](https://github.com/user-attachments/assets/c149fd34-6a06-44a1-ba60-804ea64be57b)

3. To accurately determine which country generates the highest music sales, we must first ensure all outstanding sales are properly invoiced. Our analysis of the 1970s data reveals that the USA led in invoice payments with approximately 131, followed by Canada with around 76, and Brazil ranking third with roughly 61 invoices paid.

![graph_visualiser-1750824644406](https://github.com/user-attachments/assets/6679dc8b-cffb-4aad-99a3-b553ca55ea40)

4. Complementing these sales trends, the musical content popular during the 1970s also showcased a unique character. While contemporary music features diverse global hits like "Despacito" and "Shape of You," the musical landscape of the 1970s was distinctly different, primarily dominated by rock music. During that decade, several iconic rock tracks garnered significant attention. Among the top-performing songs, listed with their respective popularity counts, were:

33: "War Pigs"

14: "Are You Experienced?"

14: "Changes"

14: "Highway Chile"

13: "Hey Joe"

13: "Third Stone From The Sun"

13: "Put The Finger On You"

12: "Radio/Video"

12: "We Are The Champions"

12: "Love Or Confusion"

![most_loved_track](https://github.com/user-attachments/assets/622403d0-30f5-4cd1-ae5f-84d12a36b543)

5. In the 1970s, an essential aspect of understanding music consumption involved a detailed sales data analysis across different cities. This analysis aimed to identify which urban centers purchased the most tracks and, crucially, to investigate if there was a correlation with cities that hosted significant live concerts. This correlation could shed light on the impact of live performances on local music sales during that era.
   
![Screenshot 2025-06-25 101033](https://github.com/user-attachments/assets/803979a1-c748-4113-828a-ede49696b70c)

6. To understand our highest-value customers, this analysis reveals Madhav R. as the top spender with $144.54, Helena Holý as the second highest at $128.70, and Hugh O'Reilly as the third, spending $114.84.
7. Based on a key popularity metric from the 1970s, Led Zeppelin (114), U2 (112), and Deep Purple (92) stand out as the top-performing rock artists, showcasing the era's dominant musical influences.

![Screenshot 2025-06-25 102543](https://github.com/user-attachments/assets/7e0e5dca-cf0c-4504-8570-3fe6fc72fa7e)

8. In the groovy year of 1970, if we were looking at this "Top 10 Invoice Cities" pie chart, here's how we'd break it down:

Alright cats and kittens, gather 'round, let's dig into this far-out chart showing where all the invoices are coming from. This ain't no disco ball, but it's shining a light on the top ten cities raking in the dough!

Dublin is the undisputed king of the hill, man! With a whopping 26% of the invoices, it's clear Dublin is where it's at. They're making more noise than a Led Zeppelin concert!

Then you've got Prague, pulling in a solid 23%. That's a strong second, real respectable. Looks like business is boomin' over there too.

Next up, we got Toronto, chipping in with 16%. Canada's got some serious hustle, that's for sure.

Orlando is showing up with a cool 12%. Maybe it's all those orange groves or something, but they're getting their share.

Bordeaux is holding steady at 8%, same as Paris. Looks like those French cities are keeping a steady rhythm, not too flashy, but getting the job done.

And then we got Fort Worth, bringing in 2%. They're on the map, making a little noise.

Way down at the bottom, just barely in the top ten, we've got Winnipeg with 4% and MontrÃ©al with a humble 1%. Hey, every little bit counts, right? They're still getting some action, even if it's not a lot of bread.

![Screenshot 2025-06-24 191204](https://github.com/user-attachments/assets/020cf0f9-71ea-449a-af5f-3f77d4b37720)

### SUMMARY - 
This music sales analysis, viewed through the lens of the 1970s, paints a clear picture:

1. Rock was the undisputed king: It wasn't just a genre; it was a cultural phenomenon that dominated sales and customer preference. Promotional strategies, if implemented in the '70s, would have been wise to lean heavily into rock artists and their widespread appeal.
2. Geographic hotspots are key: The USA, Canada, and Brazil were the big players in terms of invoice volume, indicating strong markets for music sales. Within cities, Dublin stood out as a particularly robust market. Understanding these geographic strongholds is crucial for targeted marketing.
3. Identifying top customers and artists is vital: Knowing who the biggest spenders are (like Madhav R.) and which artists are generating the most buzz (Led Zeppelin, U2, Deep Purple) allows for focused marketing efforts and artist development.
4. Employee structure matters: Having a clear senior-most employee like Mohan Madan ensures strong leadership and direction in the music business.
Track popularity drives sales: The analysis of "most loved tracks" and longest durations helps in understanding what resonates with the audience, guiding future music production and marketing.
