SELECT * FROM owners LEFT JOIN vehicles ON owner.id = vehicles.owner_id;


SELECT first_name,last_name, 
    COUNT(*) FROM owners 
    RIGHT JOIN vehicles ON owners.id = vehicles.owner_id 
    GROUP BY first_name, last_name 
    ORDER BY first_name ASC;


SELECT 
  first_name, last_name, 
  ROUND(AVG(price)) as average_price, 
  COUNT(owner_id) 
FROM owners
JOIN vehicles on owners.id=vehicles.owner_id 
GROUP BY 
  (first_name, last_name) 
HAVING 
  COUNT(owner_id) > 1 AND ROUND(AVG(price)) > 10000 
ORDER BY first_name DESC;