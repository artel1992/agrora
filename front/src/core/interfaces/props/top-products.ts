export interface Product {
    title: string
    subtitle: string
    price: string
    img: string
}

export interface TopProductsProps {
    products: Product[]
}