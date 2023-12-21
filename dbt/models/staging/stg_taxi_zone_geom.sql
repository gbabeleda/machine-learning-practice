with 

source as (

    select * from {{ source('new_york_taxi_trips', 'taxi_zone_geom') }}

),

renamed as (

    select
        zone_id,
        zone_name,
        borough,
        zone_geom

    from source

)

select * from renamed
