# Clicoh

## Descripción
*Prueba de conocimiento con Django Rest Framework*

## Endpoints

### Productos
| Método | Endpoint | Descripción |
| ------ | ------ | ------ |
| GET | /api/products/ | Listado de Productos |
| GET | /api/products/pk/ | Producto Especifico |
| PUT | /api/products/pk/ | Actualizar Producto |
| POST | /api/products/ | Crear Producto |
| Delete | /api/products/pk/ | Eliminar Producto |

#### Producto

```javascript
{
    id: 1,
    name: "Bicicleta",
    price: 15700
}
```

### Ordenes
| Método | Endpoint | Descripción |
| ------ | ------ | ------ |
| GET | /api/orders/ | Listado de Ordenes |
| GET | /api/orders/pk/ | Orden Especifica |
| POST | /api/orders/ | Crear Orden |
| PUT | /api/orders/pk/ | Actualizar Orden |
| DELETE | /api/orders/pk/ | Eliminar Orden |

#### Orden

```javascript
{
    id: 1,
    date_time: "2021/06/30 23:26:42",
}
```

### Detalles de Ordenes
| Método | Endpoint | Descripción |
| ------ | ------ | ------ |
| GET | /api/orderdetails/ | Listado de Detalles de Ordenes |
| GET | /api/orderdetails/pk/ | Detalle de Orden Especifico |
| POST | /api/orderdetails/ | Crear Detalle de Orden |
| PUT | /api/orderdetails/pk/ | Actualizar Detalle de Orden |
| DELETE | /api/orderdetails/pk/ | Eliminar Detalle de Orden |

#### Detalle

```javascript
{
    id: 1,
    quantity: 20,
    price: 385.2,
    order_id: 1,
    product_id: 2
}
```
