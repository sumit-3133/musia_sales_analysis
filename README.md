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

![graph_visualiser-1750826068426](https://github.com/user-attachments/assets/0c5b078b-bb6a-47fd-901d-8728d65e2795)
