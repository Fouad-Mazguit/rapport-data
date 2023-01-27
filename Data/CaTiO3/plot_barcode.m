function [handle] = plot_barcode(file, options)

    
    if (~exist('options', 'var'))
        options = struct;
    end

    if (isfield(options, 'min_filtration_value'))
        min_filtration_value = options.min_filtration_value;
    end
    
    if (isfield(options, 'max_filtration_value'))
        max_filtration_value = options.max_filtration_value;
    end
    
    if (isfield(options, 'min_dimension'))
        min_dimension = options.min_dimension;
    else
        min_dimension = 0;
    end
    
    if (isfield(options, 'max_dimension'))
        max_dimension = options.max_dimension;
    else
        max_dimension = 2;
    end
    
    if (isfield(options, 'filename'))
        filename = options.filename;
    else
        if (isfield(options, 'caption'))
            filename = options.caption;
        end
    end
    
    if (isfield(options, 'caption'))
        caption = options.caption;
    else
        if (isfield(options, 'filename'))
            caption = options.filename;
        end
    end
    
    if (isfield(options, 'file_format'))
        file_format = options.file_format;
    else
        file_format = 'png';
    end
    
    if (isfield(options, 'side_by_side'))
        side_by_side = options.side_by_side;
    else
        side_by_side = false;
    end
    
      
    vfont= 30;   %%%%%%% font size
    linw=3;      %%%%%%%%% line width  5
    
 
    line_width = 1.0;
    
    betti = load('ABX3_gdalpha');
    betti = {betti.betti0, betti.betti1, betti.betti2};
    
    import edu.stanford.math.plex4.*;
    
    threshold = 1e20;
    epsilon = 1e-6;
    
    max_finite_endpoint = -threshold;
    min_finite_endpoint = threshold;
        
    left_infinite_interval_found = 0;
    right_infinite_interval_found = 0;
        
    for dimension = min_dimension:max_dimension
        endpoints = betti(dimension+1);
        endpoints = endpoints{1,1};

        num_intervals = size(endpoints, 1);
       
        
        for i = 1:num_intervals
            start = endpoints(i, 1);
            finish = endpoints(i, 2);
            
            if (finish >= threshold)
                right_infinite_interval_found = 1;
            end
            
            if (start <= -threshold)
                left_infinite_interval_found = 1;
            end
            
            if (finish < threshold && finish > max_finite_endpoint)
                max_finite_endpoint = finish;
            end
            
            if (start < threshold && start > max_finite_endpoint)
                max_finite_endpoint = start;
            end
            
            if (start > -threshold && start < min_finite_endpoint)
                min_finite_endpoint = start;
            end
            
            if (finish > -threshold && finish < min_finite_endpoint)
                min_finite_endpoint = finish;
            end
        end
        
    end
    
    handle = figure;
    hold on;
    
    if (exist('max_filtration_value', 'var'))
        x_max = max_filtration_value;
    elseif (right_infinite_interval_found)
        x_max = max_finite_endpoint + 0.2 * (max_finite_endpoint - min_finite_endpoint);
    else
        x_max = max_finite_endpoint;
    end
    
    if (exist('min_filtration_value', 'var'))
        x_min = min_filtration_value;
    elseif (left_infinite_interval_found)
        x_min = min_finite_endpoint - 0.2 * (max_finite_endpoint - min_finite_endpoint);
    else
        x_min = min_finite_endpoint;
    end
    
    point_width = 0.006 * (x_max - x_min);
    
    for dimension = min_dimension:max_dimension
        endpoints = betti(dimension+1);
        endpoints = endpoints{1,1};
        num_intervals = size(endpoints, 1);
        
        if (side_by_side)
            subhandle = subplot(1, max_dimension + 1 - min_dimension, dimension + 1 - min_dimension);
        else
            subhandle = subplot(max_dimension + 1 - min_dimension, 1, dimension + 1 - min_dimension);
        end
        
        for i = 1:num_intervals
            start = endpoints(i, 1);
            finish = endpoints(i, 2);
            y = num_intervals - i + 1;
            
            if (finish >= threshold && start <= -threshold)
                line([x_min, x_max], [y, y], 'LineWidth', line_width);
                line([x_min, x_min], [y, y], 'Marker', '<', 'LineWidth', line_width);
                line([x_max, x_max], [y, y], 'Marker', '>', 'LineWidth', line_width);
            end
            
            if (finish >= threshold && start > -threshold)
                line([start, x_max], [y, y], 'LineWidth', line_width);
                line([x_max, x_max], [y, y], 'Marker', '>', 'LineWidth', line_width);
            end
            
            if (finish < threshold && start <= -threshold)
                line([x_min, finish], [y, y], 'LineWidth', line_width);
                line([x_min, x_min], [y, y], 'Marker', '<', 'LineWidth', line_width);
            end
            
            if (finish < threshold && start > -threshold)
                if (abs(finish - start) < epsilon)
                    line([start - 0.5 * point_width, finish + 0.5 * point_width], [y, y], 'LineWidth', line_width);
                else
                    line([start, finish], [y, y], 'LineWidth', line_width);
                end
            end
        end
        
         axis([x_min, x_max, 0, num_intervals + 1]);
        % axis([0.08, 0.21, 0, num_intervals + 1]);
        % set(subhandle,'XTick',[0.10,0.15,0.20],'LineWidth',0.1);
        %set(subhandle,'YTick',[],'LineWidth',0.1);
        set(subhandle,'XGrid','off','YGrid','off','LineWidth',linw,'FontSize',vfont);
     
        if(dimension == 0)
        if (exist('caption', 'var'))
         %   title(sprintf('%s', caption),'FontSize',vfont);
        else
          %  ylabel(sprintf('Dim %d', dimension),'FontSize',vfont);
        end
        end 
    end
    
    hold off;
    
    if (exist('filename', 'var'))
        saveas(handle, filename, file_format);
    end
end
