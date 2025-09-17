"""
Fotran views URL Configuration
"""
from rest_framework.response import Response
from .serializer import FortranResultsSerializer
from drf_spectacular.utils import extend_schema, OpenApiTypes
from fortran import computation
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.decorators import api_view, parser_classes

@extend_schema(
        summary="Generate Fortran Results Automatically",
        request=FortranResultsSerializer,
        responses=OpenApiTypes.OBJECT
    )
@api_view(['Get'])
def get_fortran(request):
    result = computation.computefotranAutomatically()
    data = {
        'Mass flow rate, fluid C1 (kg/h)': result[0] * 3.6E+03,
        'Global heat flux, fluid C1 (kW)': result[1] / 1.E+03,
        'Pressure drop, fluid C1 (kPa)': result[2] / 1.E+03,
        'Inlet temperature, fluid C1 (deg C)': result[3],
        'Outlet temperature, fluid C1 (deg C)': result[4],
        'Inlet vapor quality, fluid C1 (/)': result[5],
        'Outlet vapor quality, fluid C1 (/)': result[6],
        'Mass flow rate, fluid C2 (kg/h)': result[7] * 3.6E+03,
        'Global heat flux, fluid C2 (kW)': result[8] / 1.E+03,
        'Pressure drop, fluid C2 (kPa)': result[9] / 1.E+03,
        'Inlet temperature, fluid C2 (deg C)': result[10],
        'Outlet temperature, fluid C2 (deg C)': result[11],
        'Inlet vapor quality, fluid C2 (/)': result[12],
        'Outlet vapor quality, fluid C2 (/)': result[13],
        'Velocity, fluid C3 (m/s)': result[14],
        'Global heat flux, fluid C3 (kW)': result[15] / 1.E+03,
        'Pressure drop, fluid C3 (Pa)': result[16],
        'Inlet temperature, fluid C3 (deg C)': result[17],
        'Outlet temperature, fluid C3 (deg C)': result[18],
        'Error message (INT)': round(result[19])
    }
    return Response(data)

@extend_schema(
        summary="Compute Fortran Results Manually",
        request=FortranResultsSerializer,
        responses=OpenApiTypes.OBJECT
    )
@api_view(['POST'])
# @parser_classes([FormParser, MultiPartParser, JSONParser])
def create_fotran(request, *args, **kwargs):
    print(f"Request Data: {request.data}")
    # Validate and process the incoming data
    serializer = FortranResultsSerializer(data=request.data)
    if serializer.is_valid():
        # Call the function to compute results manually
        result = computation.computefotranManually(serializer.validated_data)

        data = {
        'Mass flow rate, fluid C1 (kg/h)': result[0] * 3.6E+03,
        'Global heat flux, fluid C1 (kW)': result[1] / 1.E+03,
        'Pressure drop, fluid C1 (kPa)': result[2] / 1.E+03,
        'Inlet temperature, fluid C1 (deg C)': result[3],
        'Outlet temperature, fluid C1 (deg C)': result[4],
        'Inlet vapor quality, fluid C1 (/)': result[5],
        'Outlet vapor quality, fluid C1 (/)': result[6],
        'Mass flow rate, fluid C2 (kg/h)': result[7] * 3.6E+03,
        'Global heat flux, fluid C2 (kW)': result[8] / 1.E+03,
        'Pressure drop, fluid C2 (kPa)': result[9] / 1.E+03,
        'Inlet temperature, fluid C2 (deg C)': result[10],
        'Outlet temperature, fluid C2 (deg C)': result[11],
        'Inlet vapor quality, fluid C2 (/)': result[12],
        'Outlet vapor quality, fluid C2 (/)': result[13],
        'Velocity, fluid C3 (m/s)': result[14],
        'Global heat flux, fluid C3 (kW)': result[15] / 1.E+03,
        'Pressure drop, fluid C3 (Pa)': result[16],
        'Inlet temperature, fluid C3 (deg C)': result[17],
        'Outlet temperature, fluid C3 (deg C)': result[18],
        'Error message (INT)': round(result[19])
        }
        print(f"Computed Data: {data}")
        return Response(data, status=201)
    return Response(serializer.errors, status=400)

