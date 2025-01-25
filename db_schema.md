# Database Design

This document outlines the schema design for a PostgreSQL database managing products, their clusters, manufacturers, and cluster summaries.

---

## **Schema Overview**

The database includes the following tables:

1. **`Products`**: Stores details of individual products, including their manufacturer and cluster association.
2. **`Manufacturers`**: Stores details of manufacturers.
3. **`Products_Salts`**: Maps products to their salts.
4. **`Cluster_Summary`**: Stores aggregated information about product clusters.

---

## **Tables and Schema**

### 1. **`Products`**
This table contains detailed information about products.

| Column               | Data Type      | Constraints                          |
|----------------------|----------------|--------------------------------------|
| `id`                 | SERIAL         | Primary Key                          |
| `name`               | TEXT           | Not Null                             |
| `source`             | INT            | Foreign Key → `Manufacturers(id)`    |
| `prescription_required` | BOOLEAN      | Default `FALSE`                      |
| `retail_price`       | NUMERIC(10, 2) | Not Null |
| `discounted_price`       | NUMERIC(10, 2) | Not Null |
| `packaging_form`     | TEXT           |                                      |
| `quantity_num`       | NUMERIC(10, 2) | Not Null |
| `cluster`            | INT            | Foreign Key → `Cluster_Summary(cluster_id)` |

**Foreign Key Relationships**:
- `source` references `Manufacturers(manufacturer_id)`.
- `cluster` references `Cluster_Summary(cluster_id)`.

---

### 2. **`Manufacturers`**
This table stores details of manufacturers.

| Column              | Data Type      | Constraints        |
|---------------------|----------------|--------------------|
| `manufacturer_id`   | SERIAL         | Primary Key        |
| `manufacturer_name` | TEXT           | UNIQUE, Not Null   |

---

### 3. **`Products_Salts`**
This table maps products to the salts they contain.

| Column      | Data Type | Constraints                  |
|-------------|-----------|------------------------------|
| `product_id`| INT       | Foreign Key → `Products(id)` |
| `salt_name` | TEXT      | Primary Key (with `product_id`) |

**Composite Primary Key**: (`product_id`, `salt_name`)

**Foreign Key Relationships**:
- `product_id` references `Products(id)`.
---

### 4. **`Cluster_Summary`**
This table stores aggregated data about product clusters.

| Column                  | Data Type      | Constraints                          |
|-------------------------|----------------|--------------------------------------|
| `cluster_id`            | INT            | Primary Key                          |
| `product_count`         | INT            | Not Null |
| `unique_manufacturers`  | INT            | Not Null |
| `most_frequent_medicine`| TEXT           |                                      |

---

## **Relationships**

- **Products and Manufacturers**: Each product has a single manufacturer (`Products.source` → `Manufacturers.manufacturer_id`).
- **Products and Clusters**: A product belongs to one cluster (`Products.cluster` → `Cluster_Summary.cluster_id`).
- **Products and Salts**: A product can contain multiple salts, represented in the `Products_Salts` table.
