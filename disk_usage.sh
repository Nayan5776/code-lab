disk_usage_percent=85
echo "The disk space is $disk_usage_percent%."
if [ "$disk_usage_percent" -gt 80 ]; then
    echo "Warning: Disk usage is at $disk_usage_percent%, which exceeds the threshold!"
else
    echo "$disk_usage_percent% Disk usage is below the threshold"
fi