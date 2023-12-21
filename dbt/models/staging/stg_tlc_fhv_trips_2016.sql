with 

source as (

    select * from {{ source('new_york_taxi_trips', 'tlc_fhv_trips_2016') }}

),

renamed as (

    select
        location_id,
        pickup_datetime,
        dispatching_base_num,
        borough,
        zone,
        service_zone

    from source

)

select * from renamed
