import folium
from folium.plugins import MarkerCluster, MousePosition

m = folium.Map(location=(45, -122),zoom_start=1)

marker_cluster = MarkerCluster(control=0).add_to(m)

MousePosition().add_to(m)


folium.Marker(
	location=[40.71663,-73.99974],
	icon=folium.Icon(color="red New-York snack-bar", icon="remove-sign"),
	tooltip="snack bar"
).add_to(marker_cluster)

folium.Marker(
	location=[40.8837,-74.05598],
	icon=folium.Icon(color="green New-York medical-center", icon="ok-sign"),
	# data-toggle="modal" data-target="#myModal"
	tooltip="hospital"
).add_to(marker_cluster)

folium.Marker(
	location=[40.84622, -74.06578],
	icon=folium.Icon(color="green New-York Teterboro-airport", icon="ok-sign"),
	tooltip="airport"
).add_to(marker_cluster)
