This is a simple web app built with Flask and PostgreSQL, containerized using Docker. It provides routes to add and delete records in a PostgreSQL database.

## Routes

1. **Add a record**:  
   Adds "DevOps" to the database.  
   `GET /add`

2. **Delete a record**:  
   Deletes one "DevOps" record.  
   `GET /delete`

## How to Run

1. **Start PostgreSQL**

2. **Start Flask App**
   
3. **Test**:
   - Add: `http://[server-ip]:5000/add`
   - Delete: `http://[server-ip]:5000/delete`

## Check Database

Connect to PostgreSQL:

```bash
docker exec -it my_postgres psql -U vika_test -d testdb
```

Run query to view records:

```sql
SELECT * FROM test_table;
```

```
