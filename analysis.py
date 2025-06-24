import psycopg2
from dotenv import load_dotenv
import os

import psycopg2.extras

load_dotenv()

hostname = os.getenv("HOSTNAME")
database = os.getenv("DATABASE")
username = "postgres"
pwd = os.getenv("PWD")
port_id = os.getenv("PORT")
cur = None
conn = None

def connect_to_postgresql():
    """Connects to a PostgreSQL database and returns the connection and cursor."""
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            user=username,
            password=pwd,
            host=hostname,
            port=port_id,
            database=database
        )
        cursor = connection.cursor()
        print("PostgreSQL database connection successful!")
        return connection, cursor
    except Exception as error:
        print(error)
        return None, None
    
def close_connection(connection, cursor):
    """Closes the PostgreSQL database connection."""
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("PostgreSQL connection closed.")

if __name__ == "__main__":
    conn, cur = connect_to_postgresql()

    if conn and cur:
        try:
            """cur.execute("SELECT * from album where album_id = %s;", ('1',))"""
            
            #1. Who is the senior most employee based on the job title?
            sql_query = """
                        SELECT first_name,last_name,levels
                        FROM employee
                        ORDER BY levels desc limit 1;
                        """
            cur.execute(sql_query)            
            query1 = cur.fetchall()
        
            #2. Which countries have the most Invoices?
            sql_query = """
                        SELECT Count(*), billing_country
                        FROM invoice
                        GROUP BY billing_country
                        ORDER BY count desc;
                        """
            cur.execute(sql_query)
            query2 = cur.fetchall()

            #3. Which track love's the customer more than other?
            sql_query = """
                        SELECT Count(t.name) as total,t.name
                        from track as t
                        inner join invoice_line as il ON t.track_id = il.track_id
                        inner join invoice as inv ON il.invoice_id = inv.invoice_id
                        inner join customer as cus ON inv.customer_id = cus.customer_id
                        group by t.name
                        order by total desc;
                        """
            cur.execute(sql_query)
            query3 = cur.fetchall()

            #4. What are top 3 values of total Invoices?
            sql_query = """
                        SELECT total
                        FROM invoice
                        ORDER BY total desc;
                        """           
            cur.execute(sql_query) # we also use the limit to fetch 3 values.
            query4 = cur.fetchmany(3)

            #5. Which city has the best customer?
            sql_query = """
                        SELECT sum(total) as total_of_invoice, billing_city
                        FROM invoice
                        GROUP BY billing_city
                        ORDER BY total_of_invoice desc;
                        """
            cur.execute(sql_query)         
            query5 = cur.fetchone()

            #6. Who is the the best customer?
            sql_query = """
                        SELECT customer.customer_id,customer.first_name,customer.last_name,sum(invoice.total)as total_of_invoice
                        FROM customer
                        INNER JOIN invoice on customer.customer_id = invoice.customer_id 
                        GROUP BY customer.customer_id
                        ORDER BY total_of_invoice desc;
                        """
            cur.execute(sql_query)
            query6 = cur.fetchone()
            
            #7. Return the details of the customer who loves the "Rock" music?
            search = "%Rock%"
            """cur.execute("Select Distinct email,first_name,last_name,genre from customer inner join invoice on customer.customer_id = invoice.customer_id inner join invoice_line on invoice.invoice_id = invoice_line.invoice_id inner join track on invoice_line.track_id = track.track_id inner join genre on track.genre_id = genre.genre_id where genre.name like %s order by email",(search,))"""
            cur.execute("Select Distinct email,first_name,last_name from customer inner join invoice on customer.customer_id = invoice.customer_id inner join invoice_line on invoice.invoice_id = invoice_line.invoice_id where track_id in(select track_id from track inner join genre on track.genre_id = genre.genre_id where genre.name like %s) order by email",(search,))
            query7 = cur.fetchall()
            
            #8. Return the details of the artist who have written the most "Rock" music?
            cur.execute("Select artist.artist_id,artist.name,count(artist.artist_id) as total_number_of_song from artist inner join album on artist.artist_id = album.artist_id inner join track on album.album_id = track.album_id inner join genre on track.genre_id = genre.genre_id where genre.name like %s group by artist.artist_id order by total_number_of_song desc",(search,))
            query8 = cur.fetchmany(10)

            #9. Return the track name and duration that have a longest duration?
            sql_query = """
                        SELECT name,milliseconds
                        FROM track
                        WHERE milliseconds > (SELECT AVG(milliseconds) AS avg_track_length FROM track )
                        ORDER BY milliseconds DESC;
                        """
            cur.execute(sql_query)
            query9 = cur.fetchmany(5)

            #10. Most popular genre of the customer?
            sql_query = """
                        SELECT Count(genre.name) as total,genre.name
                        from track as t
                        inner join genre on genre.genre_id = t.genre_id
                        inner join invoice_line as il ON t.track_id = il.track_id
                        inner join invoice as inv ON il.invoice_id = inv.invoice_id
                        inner join customer as cus ON inv.customer_id = cus.customer_id
                        group by genre.name
                        order by total desc;
                        """
            cur.execute(sql_query)
            query10 = cur.fetchall()


            print(f"PostgreSQL database : {query8}")


        except Exception as error:
            print(f"Error executing query: {error}")
            conn.rollback() # Rollback changes if an error occurs3
        finally:
            close_connection(conn, cur)

