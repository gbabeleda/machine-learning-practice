with 

source as (

    select * from {{ source('new_york_taxi_trips', 'tlc_fhv_trips_2017') }}

),

renamed as (

    select
        location_id,
        pickup_datetime,
        dispatching_base_num,
        borough,
        zone,
        service_zone,
        dropoff_datetime,
        dropoff_location_id,
        dropoff_borough,
        dropoff_zone,
        dropoff_service_zone

    from source

)

select * from renamed
